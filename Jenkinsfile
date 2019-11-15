node ('master') {
    stage('Checkout'){
        checkout scm
        echo "Calling Robot Job"
        sh "pwd"
        sh "ls"
        sh "robot -d Results Tests/Front_Office.robot"
    }
}