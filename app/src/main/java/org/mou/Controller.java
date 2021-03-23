package org.mou;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Hyperlink;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;


import java.awt.*;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.ResourceBundle;

public class Controller extends Application implements Initializable {
    @FXML
    private Hyperlink getGitHub;
    @FXML
    private Hyperlink reportBugIssue;
    @FXML
    private AnchorPane uploadItemsContainer;
    @FXML
    private Button uploadPhotoBttn;
    @FXML
    private Button stopBttn;
    @FXML
    private Button startBttn;

    private Desktop desktop = Desktop.getDesktop();


    /**
     * This initializes the functionality or actions of each of the declared user interface
     * object that is accessible by the user.
     * @param url This contains the pointer to the directory of an object
     * @param rb This contains the specific type of the object
     */
    @Override
    public void initialize (URL url, ResourceBundle rb){

        //goes to the GitHub repository
        getGitHub.setOnAction(e-> {
            try {
                goToGitHub();
            } catch (URISyntaxException uriSyntaxException) {
                uriSyntaxException.printStackTrace();
            } catch (IOException ioException) {
                ioException.printStackTrace();
            }
        });

        //will go to the reporting section in the GitHub
        reportBugIssue.setOnAction(e-> {
            try {
                reportAnIssue();
            } catch (URISyntaxException uriSyntaxException) {
                uriSyntaxException.printStackTrace();
            } catch (IOException ioException) {
                ioException.printStackTrace();
            }
        });

        //upload button action
        uploadPhotoBttn.setOnAction(e->getUploader());

        startBttn.setOnAction(event -> getUploader());
        stopBttn.setOnAction(event -> getUploader());
    }

    /**
     * This allows the user to get the image uploader where it calls out the other methods
     * such as storing the images inside the scroll pane.
     */
    private void getUploader() {

    }

    /**
     * This method that will call out the GitHub repository using the default web browser
     * that is set in the user's desktop
     * @throws URISyntaxException this will throw an error once the syntax inside the created URI object's parenthesis
     *                            is not a string
     * @throws IOException this will throw an error once the thrown object is null whereas the desktop browse param
     * must not be a null
     */
    @FXML
    private void goToGitHub() throws URISyntaxException, IOException {
        desktop.browse(new URI("https://github.com/raphael-di-ezmo/Mou/"));

    }

    /**
     * This method will get the user to open a new issue form from the Mou repository using
     * the default web browser that is set in the user's desktop
     * @throws URISyntaxException this will throw an error once the syntax inside the created URI object's parenthesis
     *                            is not a string
     * @throws IOException this will throw an error once the thrown object is null whereas the desktop browse param
     *                     must not be a null
     */
    @FXML
    private void reportAnIssue() throws IOException, URISyntaxException {
        desktop.browse(new URI("https://github.com/raphael-di-ezmo/Mou/issues/new"));

    }


    @FXML
    private void loadTab(ActionEvent event) throws IOException {
    }

    /**
     * This is just a default method that must be thrown for the Controller class
     * as controller class implements application
     * @param primaryStage this just contains the primary stage as a parameter
     */
    @Override
    public void start(Stage primaryStage){

    }
}
