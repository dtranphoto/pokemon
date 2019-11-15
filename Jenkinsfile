node ('master') {
    stage('Checkout'){
        checkout scm
        echo "Calling Robot Job"
       /// sh "sudo yum install python-pip"
      //  sh "sudo pip install robotframework"
      //  sh "sudo pip install robotframework-selenium2library"
        sh "pwd"
        sh " /var/lib/jenkins/workspace/robot -d Results Tests/Front_Office.robot"
    }
}