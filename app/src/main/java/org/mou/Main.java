package org.mou;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;


public class Main extends Application {


    /**
     * Main class that will call out the main fxml file
     * @param primaryStage the main stage that holds all the
     *                     user interface objects inside the window
     * @throws Exception exception that will hold whenever the FXMLLoader gets
     *                   an issue in fetching the fxml file
     */
    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("mou.fxml"));
        primaryStage.setTitle("Mou");
        primaryStage.setScene(new Scene(
                root));
        primaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
