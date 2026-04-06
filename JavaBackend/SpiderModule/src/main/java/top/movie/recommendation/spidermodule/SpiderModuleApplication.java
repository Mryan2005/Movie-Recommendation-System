package top.movie.recommendation.spidermodule;

import jep.SharedInterpreter;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpiderModuleApplication {

    public static void main(String[] args) {
        System.out.println("java.library.path = " + System.getProperty("java.library.path"));
        System.out.println("jep.pythonHome   = " + System.getProperty("jep.pythonHome"));
        System.out.println("jep.pythonLibrary= " + System.getProperty("jep.pythonLibrary"));

        // 如果这里能正常 new 出来，就代表 JEP + Python 环境 OK
        try (jep.SharedInterpreter interp = new jep.SharedInterpreter()) {
            interp.exec("import sys");
            interp.exec("print('PY EXEC:', sys.executable)");
            interp.exec("print('Hello from Python via JEP!')");
        }
        // 这个 try-with-resources 会帮你自动关闭解释器
        try (SharedInterpreter interp = new SharedInterpreter()) {

            // 1. 直接执行一段 Python 代码
            interp.exec("print('Hello from Python via JEP!')");

            // 2. 运行 Python 表达式并取回结果
            interp.exec("x = 1 + 2");

            // 借助 Number 的包容性，化解这场冲突
            int x = ((Number) interp.getValue("x")).intValue();

            System.out.println("Java got x = " + x);

            // 3. 执行多行 Python 逻辑
            interp.exec(
                    "def greet(name):\n" +
                            "    return f'你好, {name}，来自 Python 的问候'\n"
            );

            interp.set("user_name", "Mryan2005");
            interp.exec("msg = greet(user_name)");
            String msg = (String) interp.getValue("msg");

            System.out.println("Java got msg = " + msg);
        }
        SpringApplication.run(SpiderModuleApplication.class, args);
    }

}
