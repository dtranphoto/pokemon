
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
            //sh " Tests/test_env_setup.sh"
            sh "source /var/lib/jenkins/workspace/test_env_setup.sh"
            sh "echo sauce is $SAUCE_USERNAME"
            sh " /var/lib/jenkins/workspace/pytest --junitxml results.xml Tests"

        }
        catch (Exception e) {
            testfailed = 1
        }
        finally{
            //robot outputPath: 'Results', passThreshold: 95.0, unstableThreshold:75.0
            junit '*.xml'
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