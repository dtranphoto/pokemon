
testfailed = 0
def notify_failed(){
 emailext body: '''Check console output at "${env.BUILD_URL"}
''', subject: 'FAILED: JOB \'${env.JOB_NAME} ', to: 'dtranphoto101@gmail.com'
}

node ('master') {
    stage('Checkout'){
        checkout scm
        echo "Checkout Source files"
     }
    stage('Test'){
        echo "Run Robotframework Tests"
        try {
           // sh " /var/lib/jenkins/workspace/robot -d Results Tests/Pokemon.robot"
            sh "/var/lib/jenkins/workspace/pytest Tests --junitxml report.xml"
        }
        catch (Exception e) {
            testfailed = 1
              echo "Exception with pytest"
        }
        finally{
            //robot outputPath: 'Results', passThreshold: 95.0, unstableThreshold:75.0
            junit '*.xml'
              echo "Finally"
        }

    }
    stage('Report'){
        //Send Email if test fails"
        if(testfailed){
            echo "Test Failed"
            notify_failed()
        }
        else{
            echo "Test Passed"
        }
    }
}