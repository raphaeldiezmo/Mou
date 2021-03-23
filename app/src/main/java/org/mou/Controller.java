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

    private Desktop desktop = Desktop.getDesktop();

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
    }

    /**
     *
     */
    private void getUploader() {

    }

    /**
     * Method that will call out the GitHub repository using the default web browser
     * of user's preferences
     * @throws URISyntaxException
     * @throws IOException
     */
    @FXML
    private void goToGitHub() throws URISyntaxException, IOException {
        desktop.browse(new URI("https://github.com/raphael-di-ezmo/Mou/"));

    }

    @FXML
    private void reportAnIssue() throws URISyntaxException, IOException, URISyntaxException {
        desktop.browse(new URI("https://github.com/raphael-di-ezmo/Mou/issues/new"));

    }

    @FXML
    private void loadTab(ActionEvent event) throws IOException {
    }
    @Override
    public void start(Stage primaryStage) throws Exception {

    }

}
