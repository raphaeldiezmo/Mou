<h1 align="center" style="color:#0bcadb">Contribution Guidelines</h1>
<p align="center"><img src="/logo/Mou.png" alt="mou-logo" width="120px" height="120px" style="max-width:100%;"></p><Br>
<h2 style="color:#dba70b">Do programming?</h2>
<p>
For the IDE, we use IntelliJ. Any IDEs will do. Feel free to pick which ever you want, but<br>
another suggestion is you could either pick between the three best ones for this project;<br>
IntelliJ, Eclipse or NetBeans. All of these IDEs has advantages on their own.<br></p>

<h3 style="color:#f7525a">Requirements:</h3>
<p><a href="https://www.oracle.com/ie/java/technologies/javase-jdk15-downloads.html"> Java 15 JDK</a><br>    
<a href="https://gluonhq.com/products/javafx/">JavaFX 16 JDK</a> <br>
</p>

<p>If ever you're using IntelliJ, you might encounter few issues. To avoid those issues, install<br>
the required SDK versions to your system. After installing them, follow these steps below and make <br>
sure you have done it correctly otherwise you might encounter some problems on running a JavaFX on<br>
your build.</p>

<p>NOTE: <i>To make your life easier to code, better off to open the project and locate the <b>app</b><br>
 directory instead of opening the whole <b>Mou</b> project</i>
<br><br>
 If you have any errors on gradle please do send an issue report, while fixing it, please do these steps</p>

<h3 style="color:#dba70b"> Setting up the SDKs + Libraries </h3>
<p>
Locate the File > Project > check Project SDK: [and pick 11+ JDK version of Java] <br>
 - Project language level: choose default <br>
 - Project compiler output: [Path\Mou\app\out] -> <b>dont forget to change the "Path"<b><br>
 - Go to Modules > check the Source Folder if it's correct, MUST BE <b>app\src</b><br>
 - Check the libraries > Add > Locate your JavaFX 11+ version installed and locate the lib folder<br>
 - Apply and Ok</p>
<h3 style="color:#dba70b">Edit Configuration </h3>
<p >
 -  Check the module version <br>
 -  At the Modify options located at top left, click the Add VM options.</p>
 <h4 >THIS IS A MUST, otherwise you will get some errors.</h4>
 <p>
 -  Add this module : --module-path="PATH/javafx-sdk-15.0.1/lib" --add-modules=javafx.controls,javafx.fxml
</p>

<h2 style="color:#dba70b">Want to do the functionality of the application part?</h2>
<p>In this part, you will be tackling some programming an automation.</p>
<h3 style="color:#dba70b">Requirements:</h3>
<p>
 <a href="https://www.python.org/downloads/">Python 3+</a><br><br>
 Don't forget to install the following modules<br>
 - pywin32 module<br>
 - opencv  module<br>
 - tensorflow module<br>
    </p>

 <h3 align="center">Gladly appreciate your contribution!!</h3>

