node ('master') {
    stage('Checkout'){
        checkout scm
        echo "Calling Robot Job"
        sh "yum install python-pip"
        sh "pip install robotframework"
        sh "pip install robotframework-selenium2library"
        sh "which robot"
        sh "robot -d Results Tests/Front_Office.robot"
    }
}