<h1 align="center">Instructions on How to contribute</h1>
<span align="center"><img src="/logo/Mou.png" alt="mou-logo" width="120px" height="120px" style="max-width:100%;"></span><Br>
<h2 align="center">Do programming?</h2>
<p align="center">
For the IDE, we use IntelliJ. Any IDEs will do. Feel free to pick which ever you want, but<br>
another suggestion is you could either pick between the three best ones for this project;<br>
IntelliJ, Eclipse or NetBeans. All of these IDEs has advantages on their own.<br></p>

<h3 align="center">Requirements:</h3>
<p align="center"><a href="https://www.oracle.com/ie/java/technologies/javase-jdk15-downloads.html"> Java 11+ JDK</a><br>    
<a href="https://gluonhq.com/products/javafx/">JavaFX 11+ JDK</a> <br>
</p>

<p align="center">If ever you're using IntelliJ, you might encounter few issues. To avoid those issues, install<br>
the required SDK versions to your system. After installing them, follow these steps below and make <br>
sure you have done it correctly other wise you might encounter some problems on running a JavaFX on<br>
your build.</p>

<h3 align="center" style="color:blue"> Setting up the SDKs + Libraries </h3>
<p align="center">
Locate the File > Project > check Project SDK: [and pick 11+ JDK version of Java] <br>
 - Project language level: choose default <br>
 - Project compiler output: [Path\Mou\app\out] -> <b>dont forget to change the "Path"<b><br>
 - Go to Modules > check the Source Folder if it's correct, MUST BE <b>app\src</b><br>
 - Check the libraries > Add > Locate your JavaFX 11+ version installed and locate the lib folder<br>
 - Apply and Ok</p>
<h3 align="center">Edit Configuration </h3>
<p align="center">
 -  Check the module version <br>
 -  At the Modify options located at top left, click the Add VM options.</p>
 <h4 align="center">THIS IS A MUST, otherwise you will get some errors.</h4>
 <p align="center">
 -  Add this module : --module-path="PATH/javafx-sdk-15.0.1/lib" --add-modules=javafx.controls,javafx.fxml
</p>
 
 <h3 align="center">Gladly appreciate your contribution!!</h3>
