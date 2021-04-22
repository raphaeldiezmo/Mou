package org.mou;

import javafx.application.Application;
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


/**
 * Class that contains all functionality of the FXML user interface objects
 * such as Buttons, Hyperlinks, etc. This also extends the Application and
 * implements initialisable.
 */
public class Controller extends Application implements Initializable {
    @FXML
    private Hyperlink gitHubLink;
    @FXML
    private Hyperlink reportBugIssueLink;
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
     * @param url a string that represents the URL to use in fetching an object URL
     * @param rb This contains the specific type of the object
     */
    @Override
    public void initialize (URL url, ResourceBundle rb){

        //setting up an action for fetching up the GitHub Link
        gitHubLink.setOnAction(e-> {
            try {
                goToGitHub();
                //catches URI Syntax exception if it the link doesn't exist
            } catch (URISyntaxException uriSyntaxException) {
                uriSyntaxException.printStackTrace();
                //catches up some Input Ouput exception
            } catch (IOException ioException) {
                ioException.printStackTrace();
            }
        });

        //setting up an action of the report a bug link inside the
        // welcome page of the applicatiopn
        reportBugIssueLink.setOnAction(e-> {
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

        //start button event, this triggers the function of start bttn
        startBttn.setOnAction(event -> getUploader());
        stopBttn.setOnAction(event -> getUploader());
    }


    //-----------------------------------------------------------------------------------------------
    //----------------------------------- WELCOME TAB FUNCTIONALITY ---------------------------------
    //-----------------------------------------------------------------------------------------------
    /**
     * This method that will call out the GitHub repository using the default web browser
     * that is set in the user's desktop
     * @throws URISyntaxException if URI (Uniform Resource Identifier is NULL
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
     * @throws URISyntaxException if URI (Uniform Resource Identifier) is NULL
     * @throws IOException if the reading contains the failure
     */
    @FXML
    private void reportAnIssue() throws IOException, URISyntaxException {
        //calls the default browser using the stated URI
        desktop.browse(new URI("https://github.com/raphael-di-ezmo/Mou/issues/new"));
    }
    @FXML
    private void sendSuggestion(){
    }
    //-----------------------------------------------------------------------------------------------
    //-----------------------------------UPLOAD TAB FUNCTIONALITY------------------------------------
    //-----------------------------------------------------------------------------------------------
    /**
     * This method will copy a targeted file into a targeted directory
     */
    private void uploadPhoto(){

    }

    /**
     * This allows the user to get the image uploader where it calls out the other methods
     * such as storing the images inside the scroll pane.
     */
    private void getUploader() {
    }
    //-----------------------------------------------------------------------------------------------
    //------------------------------- CALLING THE PYTHON PROGRAM ------------------------------------
    //-----------------------------------------------------------------------------------------------
    private void startAutomation(){

    }
    private void stopAutomation(){

    }

    /**
     * This method runs another application program that has the functionality
     * to detect object, the executable application will be in the same directory
     * of this application otherwise it won't work and return's null
     */
    private void detectObject() throws Exception{

    }

    //-----------------------------------------------------------------------------------------------
    //--------------------- MANDATORY METHOD FOR THE IMPLEMENTED APPLICATION ------------------------
    //-----------------------------------------------------------------------------------------------

    /**
     * This is just a default method that must be thrown for the Controller class
     * as controller class implements application
     * @param primaryStage contains the primary window or container
     */
    @Override
    public void start(Stage primaryStage){

    }
}
