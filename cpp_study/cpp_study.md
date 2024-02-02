# C++ TIL

## C++는 자유롭다.
- C++ 코드 작성 시 C 스타일로 코딩하거나 C부터 이어진 표준 함수를 사용하는 것이 잘못된 것으로 인식하거나 그렇게 가르치는 사람들이 적지 않다. 예를 들어 **std::cout** 사용을 권장하고 **std::printf**는 지양해야 한다고 하거나, 언어에서 제공하는 기능임에도 사용하면 안되는 것이라고 하는 사람들도 있다. 예를 들어 **goto**는 사용하면 안된다와 같이 금지 조항을 만드는 사람들이다. **goto** 비판에 대해서는 http://en.wikipedia.org/wiki/Goto 참고한다.

1. C와 C++는 다르다. 하지만 C++는 C의 대부분을 포함한다. C++에서 C 스타일 코드를 사용하는 것은 문제 없다. 단 C에 비해 자료형을 명확히 사용해야 한다.
2. C++는 **객체지향 언어**가 아니다. 객체지향 기능을 지원하는 언어이다. C++를 절차지향 개념을 적용하여 코드를 만드는 것은 이상한 것이 아니다.
https://www.stroustrup.com/oopsla.pdf https://www.geeksforgeeks.org/c-partially-object-oriented-language
3. C부터 이어진 표준 함수를 사용하지 않아도 된다. 다만 C 표준 함수가 C++ 표준 함수에 비해 빠른 경우가 있따. 예를 들어 **std::printf**는 **std::cout**에 비해 대부분 빠르게 출력한다. 그리고 스트림 버퍼를 비워야 하는 경우가 아니면 **std::endl** 을 사용하는 것보다 **\n**을 사용하는 것이 낫다

## 프로그램의 작동 원리와 CPU
1. 프로그램의 작동 원리
    1. 프로그래머가 C언어 등의 고급 언어로 소스 코드를 작성한다.
    2. 그 소스 코드를 컴파일해 기계어인 실행 파일(.exe)로 변환한다.
    3. 프로그램이 실행될 때 실행 파일의 복사본이 메모리(주기억장치)에 올려진다.
    4. CPU가 메모리 상에 있는 exe파일을 해석하고 실행한다.
2. CPU의 메모리의 실제로는 IC(Integrated Circuit)로 불리는 전자 부품이다. IC는 많은 수의 트랜지스터로 구성된 전자회로로, 마이크로 칩이라고도 불린다.            
* 트랜지스터 : 반도체 3개 (pnp or npn)를 이어붙인 것. 증폭 작용과 스위치 작용을 한다.   
    - CPU는 크게 네 가지로 이루어져 있다.
        1. 레지스터(Register) : 명령어와 데이터를 보관하는 영역. 일종의 메모리와 같다. CPU에는 대략 20~100개 정도의 레지스터가 존재한다.
        2. 제어 장치(CU, Control Unit): 메모리의 명령어와 데이터를 읽어와 레지스터에 넣는다.
        3. 연산 장치(ALU, Arithmetic Logical Unit) : 메모리부터 읽은 데이터에 대해 산술 및 논리 연산을 한다.
        4. 클록 제너레이터(Clock Genarator): 쿼츠 무브먼트와 IC 칩으로 구성되며, 클록 신호를 발생시킨다.
        * 쿼츠 무브먼트 : 쿼츠 시계에 쓰이는 무브먼트. 석영(quartz)결정을 절단해 만든 작은 조각 양끝에 전극을 달고, 그에 전압을 걸면 주기가 일정한 진동이 일어난다.
        * 클록 신호 : CPU에 가해지는 전기적 진동(0 or 1)의 속도를 나타내는 단위로, Hz로 표기한다. 주파수가 클수록 CPU가 빠르게 작동한다.
3. ★ 메모리 ★
- 프로그래밍 언어에서 변수는 다음을 의미한다.
> 어떤 값을 저장할 수 있는 메모리 공간에 붙은 이름. 또는 그 메모리 공간 자체.
- 여기서 메모리 공간이란 보통 메인 메모리를 말한다. 이 메모리는 CPU와 연결되어 있고 명령어와 데이터를 저장하는 역할을 한다. 메인 메모리는 1바이트 단위로 구분되어 있는데, 이렇게 구분된 단위에는 주소, 번지 또는 (address)라고 부르는 숫자가 할당되어 있다. 따라서 CPU는 어드레스를 지정해 메인 메모리에 데이터를 읽고 쓴다.
* 메인 메모리란? : 주 기억장치. 프로그램이나 데이터를 보관하는 역할을 한다. 보통 DRAM(Dynamic Random Access Memory)칩을 사용한다. DRAM은 모든 주소에 대해 데이터를 읽고 쓸 수 있지만, 전원이 끊기면 모든 데이터가 사라진다는 단점이 있다.
> 정리하면 프로그램이 실행되는 구조는 다음과 같다.    
프로그램이 실행되면 제어 장치가 클록 신호에 맞춰 메모리부터 명령이나 데이터를 읽는다.    
제어 장치가 명령어를 해석하고 실행하면서 연산 장치에서 데이터가 연산되고, 그 결과에 따라 제어 장치가 컴퓨터 전체를 제어한다.


## Quick Reference Sheet (참조 시트)

### 헤더 파일 추가
```cpp
#include <headerfile> // library
#include "headerfile" // user's header
```

### 표준 라이브러리 주 사용 헤더파일

> io, algorithms, containers, concurrency

### 자료형

> bool, char, int, double    
and standard library types such as string, vector<> and so on

### 배열, 포인터, 참조자
```cpp
int arr[5] = {1, 2, 3, 4, 5};
int* p = arr;
int& r = arr[0]
```

### 주석
```cpp
// comment text
/*
    Multi-line comment text
*/
```
### 조건 분기문
```cpp
if(<conditions>) {
    <statement 1>;
}
else {
    <statement 2>
}
-----------------------
switch (<expression>)
case <constant 1>:
    <statement sequence 1>;
    break;
case <constant 2>:
    <statement sequence 2>;
    break;
//...
case <constant n>:
    <statement sequence n>;
    break;
default:
    <statement sequence n+1>;
    break;
}
```

## hello world!
- **#include** 외부 헤더파일 추가하는 전처리자(preprocessor)
- **<iostream>** 표준 라이브러리 헤더 파일
- **using std::count** namespace 내의 내용을 접근자 없이 사용
- **;** 하나의 문장을 끝마치는 문자
- **int main(int argc, char* argv[])** 함수와 매개변수 그리고 모든 프로그램의 진입점인 main 함수
- **std::cout** 템플릿 클래스로 구현된 출력스트림의 전역 객체
- **"hello, world!"** 문자열 리터럴
- **std::endl** 줄바꿈과 스트림 버퍼를 지우는 템플릿 함수
- **return** 함수의 반환값 처리
- **EXIT_SUCCESS** 값이 0인 매크로
```cpp
#include <iostream>
#include <cstdlib>

using std::cout;
using std::endl;

int main(int argc, char *argv[])
{
    std::cout << "Hello, world!" << std::endl;
    return EXIT_SUCCESS;
}
```

```cpp
#include <iostream>
#include <string>

// say what standard-library names we use
using std::cin;         using std::endl;
using std::cout;        using std::string;

int main()
{
    // ask for the person's name
    cout << "Please enter your first name: ";

    // read the name
    string name;
    cin >> name;

    // build the message that we intend to write
    const string greeting = "Hello, " + name + "!";

    // the number of blanks surrounding the greeting
    const int pad = 1;

    // the number of rows and columns to write
    const int rows = pad * 2 + 3;
    const string::size_type cols = greeting.size() + pad * 2 + 2;

    // write a blank line to separate the output from the input
    cout << endl;

    // write `rows' rows of output
    // invariant: we have written `r' rows so far
    for (int r = 0; r != rows; ++r) {

        string::size_type c = 0;

        // invariant: we have written `c' characters so far in the current row
        while (c != cols) {

            // is it time to write the greeting?
            if (r == pad + 1 && c == pad + 1) {
                cout << greeting;
                c += greeting.size();
            } else {

                // are we on the border?
                if (r == 0 || r == rows - 1 ||
                    c == 0 || c == cols - 1)
                    cout << "*";
                else
                    cout << " ";
                ++c;
            }
        }

        cout << endl;
    }

    return 0;
}
```