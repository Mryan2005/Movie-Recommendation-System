package top.movie.recommendation.spidermodule;

import jep.SharedInterpreter;
import jep.MainInterpreter;

public class JepConfig {

    public static void main(String[] args) {
        try {
            // 1. 强行指定 DLL
            String jepDllPath = "D:/A2564/projects/Movie-Recommendation-System/JavaBackend/SpiderModule/venv38/Lib/site-packages/jep/jep.dll";
            MainInterpreter.setJepLibraryPath(jepDllPath);
            System.out.println("=> Java: 已设定 DLL 路径");

            // 2. 启动 JEP
            try (SharedInterpreter interp = new SharedInterpreter()) {
                System.out.println("=> Java: JEP 解释器创建成功！Python 已经苏醒！");

                // 告诉 Python 准备一个字符串
                interp.exec("import sys");
                interp.exec("message = 'Hello from Python! 我的版本是: ' + sys.version");

                // 【关键】从 Python 把变量拿回到 Java！
                String pythonMessage = interp.getValue("message", String.class);

                // 用 Java 打印出来，Maven 绝对吞不掉
                System.out.println("=> Java 收到了 Python 的传书: " + pythonMessage);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}