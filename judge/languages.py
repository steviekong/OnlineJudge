from problem.models import ProblemIOMode


default_env = ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]

_c_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
/*
This comment is to help you read input from stdin in C.
Please ignore it incase you already know how to do that.
Ensure following line is included in header
#include <stdio.h>
Case 1: read a single integer
Ex - 2
    int n;
    scanf("%d",&n);
Case 2: read three space separated integers in a given line
Ex - 5 6 7
    int x,y,z;
    scanf("%d %d %d",&x, &y, &z);
Case 3: read an array of n space separated integers in a given line
Ex - 1 4 6 1 2 5 7 8 1 2
    for(i=0;i<n;i++){
        scanf("%d", &arr[i]);
    }
In last case(3), ensure the array 'arr' at least has n space for integers
Case 4: read a string 
Ex - "masaischool"
    scanf("%s", str);
In case 4, ensure that 'str' is a character array with sufficient space for all characters
*/
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "main.c",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 256 * 1024 * 1024,
        "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": {ProblemIOMode.standard: "c_cpp", ProblemIOMode.file: "c_cpp_file_io"},
        "env": default_env
    }
}

_c_lang_spj_compile = {
    "src_name": "spj-{spj_version}.c",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 3000,
    "max_real_time": 10000,
    "max_memory": 1024 * 1024 * 1024,
    "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}"
}

_c_lang_spj_config = {
    "exe_name": "spj-{spj_version}",
    "command": "{exe_path} {in_file_path} {user_out_file_path}",
    "seccomp_rule": "c_cpp"
}

_cpp_lang_config = {
    "template": """//PREPEND BEGIN
#include <iostream>
using namespace std;
//PREPEND END

//TEMPLATE BEGIN
/*
This comment is to help you read input from stdin in C++.
Please ignore it incase you already know how to do that.
Ensure following 2 lines are included in header
#include <iostream>
using namespace std;
Case 1: read a single integer
Ex - 2
    int x;
    cin>>x;
Case 2: read three space separated integers in a given line
Ex - 5 6 7
    int x, y, z;
    cin>>x>>y>>z;
Case 3: read an array of n space separated integers in a given line
Ex - 1 4 6 1 2 5 7 8 1 2
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
In last case(3), ensure the array 'arr' at least has n space for integers
Case 4: read a string 
Ensure #include <string> is present in header
Ex - "masaischool"
    string s;
    cin>>s;
*/
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "main.cpp",
        "exe_name": "main",
        "max_cpu_time": 10000,
        "max_real_time": 20000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++14 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": {ProblemIOMode.standard: "c_cpp", ProblemIOMode.file: "c_cpp_file_io"},
        "env": default_env
    }
}

_cpp_lang_spj_compile = {
    "src_name": "spj-{spj_version}.cpp",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 10000,
    "max_real_time": 20000,
    "max_memory": 1024 * 1024 * 1024,
    "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++14 {src_path} -lm -o {exe_path}"
}

_cpp_lang_spj_config = {
    "exe_name": "spj-{spj_version}",
    "command": "{exe_path} {in_file_path} {user_out_file_path}",
    "seccomp_rule": "c_cpp"
}

_java_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
/*
 All programs must begin in a static main method in a Main class. Do not use public classes: even Main
    class Main
    {
        public static void main (String[] args) throws java.lang.Exception
        {
            // your code goes here
            System.out.println("masai");
        }
    }
This comment is to help you read input from stdin in Java8.
Please ignore it incase you already know how to do that.
read a single integer
Ex - 2
Scanner sc = new Scanner(System.in);
int t = Integer.parseInt(sc.nextLine());
read three space separated integers in a given line
Ex - 2 3
Scanner sc = new Scanner(System.in);
String[] nextLine = sc.nextLine().split(" ");
int N = Integer.parseInt(nextLine[0]);
int C = Integer.parseInt(nextLine[1]);
read an array of space separated integers in a given line
Ex - 1 2 3 6 7 12 32 1
Scanner sc = new Scanner(System.in);
String[] numbers = sc.nextLine().split(" ");
int arr[] = new int[numbers.length];
for(int i = 0; i < numbers.length; i++)
    arr[i] = Integer.parseInt(numbers[i]);
read a string
Ex - masai
Scanner sc = new Scanner(System.in);
String s = sc.nextLine();
 */
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "Main.java",
        "exe_name": "Main",
        "max_cpu_time": 5000,
        "max_real_time": 10000,
        "max_memory": -1,
        "compile_command": "/usr/bin/javac {src_path} -d {exe_dir} -encoding UTF8"
    },
    "run": {
        "command": "/usr/bin/java -cp {exe_dir} -XX:MaxRAM={max_memory}k -Djava.security.manager -Dfile.encoding=UTF-8 "
                   "-Djava.security.policy==/etc/java_policy -Djava.awt.headless=true Main",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}


_py2_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
'''
This comment is to help you read input from stdin in Python2.
Please ignore it incase you already know how to do that.
# read a single integer
# Ex - 2
x = int(raw_input())
# read three space separated integers in a given line
# Ex - 5 6 7
a, b, c = list(map(int, raw_input().split()))
# read an array of space separated integers in a given line
# Ex - 1 4 6 1 2 5 7 8 1 2
list_of_integers = list(map(int, raw_input().split()))
# read a string
s = raw_input()
'''
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "solution.py",
        "exe_name": "solution.pyc",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/python -m py_compile {src_path}",
    },
    "run": {
        "command": "/usr/bin/python {exe_path}",
        "seccomp_rule": "general",
        "env": default_env
    }
}
_py3_lang_config = {
    "template": """//PREPEND BEGIN

//PREPEND END
//TEMPLATE BEGIN
'''
This comment is to help you read input from stdin in Python3.
Please ignore it incase you already know how to do that.
# read a single integer
# Ex - 2
x = int(input())
# read three space separated integers in a given line
# Ex - 5 6 7
a, b, c = list(map(int, input().split()))
# read an array of space separated integers in a given line
# Ex - 1 4 6 1 2 5 7 8 1 2
list_of_integers = list(map(int, input().split()))
# read a string
s = input()
'''
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "solution.py",
        "exe_name": "__pycache__/solution.cpython-36.pyc",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/python3 -m py_compile {src_path}",
    },
    "run": {
        "command": "/usr/bin/python3 {exe_path}",
        "seccomp_rule": "general",
        "env": default_env + ["PYTHONIOENCODING=utf-8"]
    }
}

_go_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "main.go",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/go build -o {exe_path} {src_path}",
        "env": ["GOCACHE=/tmp"]
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "",
        # 降低内存占用
        "env": ["GODEBUG=madvdontneed=1"] + default_env,
        "memory_limit_check_only": 1
    }
}

_js_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END
//TEMPLATE BEGIN
function runProgram(input){
    // input is the input string from stdin you must parse it yourself
    // Write your code below this comment
}
process.stdin.resume();
process.stdin.setEncoding("ascii");
let read = "";
process.stdin.on("data", function (input) {
    read += input;
});
process.stdin.on("end", function () {
    read = read.replace(/\\n$/,"")
    read = read.replace(/\\n$/,"")
   runProgram(read);
});
process.on("SIGINT", function () {
    read = read.replace(/\\n$/,"")
    runProgram(read);
    process.exit(0);
});
//TEMPLATE END
//APPEND BEGIN
//APPEND END""",
    "run": {
        "exe_name": "solution.js",
        "command": "/usr/bin/nodejs {exe_path}",
        "seccomp_rule": None,
    }
}

languages = [
    {"config": _c_lang_config, "spj": {"compile": _c_lang_spj_compile, "config": _c_lang_spj_config},
     "name": "C", "description": "GCC 5.4", "content_type": "text/x-csrc"},
    {"config": _cpp_lang_config, "spj": {"compile": _cpp_lang_spj_compile, "config": _cpp_lang_spj_config},
     "name": "C++", "description": "G++ 5.4", "content_type": "text/x-c++src"},
    {"config": _java_lang_config, "name": "Java", "description": "OpenJDK 1.8", "content_type": "text/x-java"},
    {"config": _py2_lang_config, "name": "Python2", "description": "Python 2.7", "content_type": "text/x-python"},
    {"config": _py3_lang_config, "name": "Python3", "description": "Python 3.6", "content_type": "text/x-python"},
    {"config": _go_lang_config, "name": "Golang", "description": "Golang 1.14", "content_type": "text/x-go"},
    {"config": _js_lang_config, "name": "JavaScript", "description": "Node.js 12.18.2", "content_type": "text/javascript"}
]
