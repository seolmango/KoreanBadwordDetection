"""
WordDetection 경량화 및 최적화 버전입니다.
Made by S.C.H
"""
import pickle

korean_one = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'] # 한글 초성
korean_two = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'] # 한글 중성
korean_three = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'] # 한글 종성

def detach_word(word):
    """
    word에 한글이 입력되면 초성,중성,종성으로 쪼개줍니다
    한글이 아니면 그냥 넘김니다
    """
    result = []
    askicode = ord(word[0]) - 44032
    if -1 < askicode and askicode < 11173:
        result.append([korean_one[askicode // 588],word[1]])
        result.append([korean_two[(askicode // 28) % 21],word[1]])
        if korean_three[askicode % 28] == '':
            pass
        else:
            result.append([korean_three[askicode % 28],word[1]])
    else:
        result.append(word)
    return result

def MakeBetter(x:int):
    """
    글자수가 짧을 수록 더 엄격하게 확률을 적용합니다
    """
    return 0.1**((x-3)/10)+1


class WordDetection():

    def __init__(self):

        """
        처리 과정에 필요한 데이터
        """
        self.BaseL = {} #Base layer 데이터
        self.SeemL = {} #Seem layer 데이터
        self.KeBoL = {} #KeyBorad layer 데이터
        self.PronL = {} #Pro layer 데이터


        """
        처리후 생기는 데이터
        """
        self.input = '' # 입력된 문자열
        self.WTD = [] #Token 화 , Detach 모두 완료된 입력 문자열의 리스트
        self.BwNt = [] #Token화가 되지않은 badword의 리스트
        self.BwT = [] #Token 화가 완료된 badword의 리스트
        self.Result = [] #결과 값
        

    def LoadData(self , respon = False):
        """
        각 layer들의 데이터를 로딩해옵니다
        respon이 True일시에는 해당 레이어의 값들을 return 해줍니다.
        """
        with open('WDLD.txt', 'rb') as f:
            self.BaseL = pickle.load(f)
            self.SeemL = pickle.load(f)
            self.KeBoL = pickle.load(f)
            self.PronL = pickle.load(f)
        if respon is True:
            return [self.BaseL , self.SeemL , self.KeBoL , self.PronL]
        else:
            return None

    def AddBW(self , badword:str , respon = False):
        """
        BadWord를 입력받습니다.
        입력된 값을 self.BwNt에 추가합니다
        """
        if badword in self.BwNt:
            return None
        else:
            self.BwNt.append(badword)
            if respon is True:
                return badword
            else:
                return None

    def TokenBW(self , respon = False):
        """
        badwords를 토큰화 합니다.
        """
        result = []
        for i in self.BwNt:
            iList = []
            for j in range(0,len(i)):
                Dj = detach_word([i[j],j])
                for k in range(0,len(Dj)):
                    if Dj[k][0] in self.BaseL:
                        Dj[k][0] = self.BaseL[Dj[k][0]]
                        iList.append(Dj[k])
            result.append(iList)
        self.BwT = result
        if respon is True:
            return result
        else:
            return None

    def W2NR(self):
        """
        self.input 을 자동으로 처리하여 self.WTD로 입력합니다
        """
        PassList = [' ','이']
        result = []
        word = self.input
        """
        단어 쪼개고 중복 제거
        """
        for i in range(len(word)):
            if word[i] not in PassList:
                if i == len(word)-1:
                    result.append([self.input[i],i])
                else:
                    if word[i] == word[i+1][0]:
                        pass
                    else:
                        result.append([self.input[i],i])
            else:
                pass
        """
        초성 , 중성 ,종성 분리하기
        """
        result1 = []
        for i in range(0,len(result)):
            for j in detach_word(result[i]):
                result1.append(j)
        result = result1
        result1 = [[],[],[],[]]
        for i in result:
            if i[0] in self.SeemL or i[0] in self.KeBoL or i[0] in self.PronL:
                if i[0] in self.SeemL:
                    result1[0].append((self.SeemL[i[0]],i[1]))
                else:
                    if i[0] in self.PronL:
                        result1[0].append((self.PronL[i[0]],i[1]))
                    elif i[0] in self.KeBoL:
                        result1[0].append((self.KeBoL[i[0]],i[1]))
                if i[0] in self.KeBoL:
                    result1[1].append((self.KeBoL[i[0]],i[1]))
                else:
                    if i[0] in self.SeemL:
                        result1[1].append((self.SeemL[i[0]],i[1]))
                    elif i[0] in self.PronL:
                        result1[1].append((self.PronL[i[0]],i[1]))
                if i[0] in self.PronL:
                    result1[2].append((self.PronL[i[0]],i[1]))
                else:
                    if i[0] in self.SeemL:
                        result1[2].append((self.SeemL[i[0]],i[1]))
                    elif i[0] in self.KeBoL:
                        result1[2].append((self.KeBoL[i[0]],i[1]))
            if i[0] in self.BaseL:
                result1[0].append((self.BaseL[i[0]],i[1]))
                result1[1].append((self.BaseL[i[0]],i[1]))
                result1[2].append((self.BaseL[i[0]],i[1]))
                result1[3].append((self.BaseL[i[0]],i[1]))
            else:
                pass
            
                
        result = result1
        self.WTD = result
        return None

    def word_comparing(self , compare_word , compare_badword):
        """
        compare_word에 입력된 값을 compare_badword와 비교합니다.
        compare_word와 compare_badword에 입력되는 값은 길이가 같아야하고 토큰화된 후 이여야 합니다
        """
        a = 0
        if len(compare_word) != len(compare_badword):
            raise "Cant_compare"
        for i in range(len(compare_word)):
            j = None
            for k in range(0,len(compare_word)):
                if str(compare_word[i][0])[0:2] == str(compare_badword[k][0])[0:2]:
                    if j is None:
                        j = k
                    elif abs(j-i) > abs(k-i):
                        j = k
                    else:
                        pass
            if j is not None:
                a += 0.1 / pow(2, (abs(j - i)))*(10-abs(int(str(compare_word[i][0])[2])-int(str(compare_badword[j][0])[2])))
        same = a / len(compare_badword)
        better = MakeBetter(len(compare_word))
        return same ** better
        

    def lime_compare(self, badwords , compare_word,cut_line):
        """
        compare_word 와 badwords를 비교합니다
        """

        result = []
        for cw in compare_word:
            b = []
            c = {}
            for i in range(0,len(badwords)):
                badi = badwords[i]
                for j in range(len(cw)-len(badi)+1):
                    a = self.word_comparing(cw[j:(j+len(badi))],badi)
                    comparewordstart = cw[j]
                    comparewordend = cw[(j+len(badi))-1]
                    in_list = (comparewordstart[1],comparewordend[1],a,self.BwNt[i])
                    if a>=cut_line and comparewordstart[1] not in c:
                        c[comparewordstart[1]] = (a,in_list)
                        b.append(in_list)
                    elif comparewordstart[1] in c and c[comparewordstart[1]][0] < a:
                        b.remove(c[comparewordstart[1]][1])
                        b.append(in_list)
            result.append(b)
        self.result = result
        return result        
                
if __name__ =='__main__':
    import time
    a = WordDetection()
    a.LoadData()
    f=open("Badwords.txt",'r',encoding="utf-8")
    while True:
        line = f.readline()
        if not line: break
        a.AddBW(line[0:-1])
    f.close()
    a.TokenBW()
    cutline = int(input("몇 %이상인 것만 출력할까요?"))
    while True:
        a.input=input('필터링할 문장 입력!!')
        stime = time.time()
        a.W2NR()
        a.lime_compare(a.BwT , a.WTD , cutline/100)
        print(f'테스트 문장 : {a.input}')
        b = 1
        for i in a.result:
            print('      레이어      ',b)
            for j in i:
                print(f'{a.input[j[0]:j[1]+1]}  :  ("{j[3]}"일 확률 {round(j[2]*100)}%)')
            b += 1
        print('소요시간 : ',time.time()-stime,'초')
        print("\n ==================== \n")
        
        
        

        
