package sample;

import com.sun.deploy.uitoolkit.impl.fx.HostServicesFactory;
import com.sun.javafx.application.HostServicesDelegate;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.control.Hyperlink;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.StrokeLineCap;
import javafx.scene.shape.StrokeLineJoin;
import javafx.scene.shape.StrokeType;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.List;
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

    @Override
    public void initialize (URL url, ResourceBundle rb){
        getGitHub.setOnAction(e->goToGitHub());
        reportBugIssue.setOnAction(e->reportAnIssue());
        uploadPhotoBttn.setOnAction(e->getUploader());
    }

    /**
     *
     */
    private void getUploader() {
        FileChoose fc = new FileChoose();
        //checking if it reach this stage
        //System.out.println("It goes here");
    }

    @FXML
    private void goToGitHub(){
        HostServicesDelegate hostServices = HostServicesFactory.getInstance(this);
        hostServices.showDocument("https://github.com/raphael-di-ezmo/Mou");
    }

    @FXML
    private void reportAnIssue(){
        HostServicesDelegate hostServices = HostServicesFactory.getInstance(this);
        hostServices.showDocument("https://github.com/raphael-di-ezmo/Mou/issues/new");
    }

    @FXML
    private void loadTab(ActionEvent event) throws IOException {
        //Parent root = FXMLLoader.load(uploadItemsContainer);
    }
    @Override
    public void start(Stage primaryStage) throws Exception {

    }

}
