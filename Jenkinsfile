node ('master') {
    stage('Checkout'){
        checkout scm
        echo "Calling Robot Job"
        sh "whoami"
        sh "pwd"
        sh "ls"
        sh "export $PATH=/usr/local/bin:$PATH"
        sh "which robot"
        sh "robot -d Results Tests/Front_Office.robot"
    }
}