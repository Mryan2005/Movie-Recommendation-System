SETLOCAL
SET VIRTUAL_ENV=D:\A2564\projects\Movie-Recommendation-System\JavaBackend\SpiderModule\venv38

IF NOT "%VIRTUAL_ENV%"=="" (
SET PATH="%VIRTUAL_ENV%\bin";"%JAVA_HOME%\bin";"%PATH%"
SET PYTHONHOME=%VIRTUAL_ENV%
)

SET cp="d:\a2564\projects\movie-recommendation-system\javabackend\spidermodule\venv38\Lib\site-packages\jep\jep-4.2.2.jar"
IF DEFINED CLASSPATH (
SET cp=%cp%;%CLASSPATH%
)

SET jni_path="d:\a2564\projects\movie-recommendation-system\javabackend\spidermodule\venv38\Lib\site-packages\jep"

SET args=%*
IF "%args%"=="" (
SET args="d:\a2564\projects\movie-recommendation-system\javabackend\spidermodule\venv38\Lib\site-packages\jep\console.py"
)

java -classpath %cp% -Djava.library.path=%jni_path% jep.Run %args%
ENDLOCAL
