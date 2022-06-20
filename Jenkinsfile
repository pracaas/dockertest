pipeline {
  agent any
  stages {
    stage ("Initializing"){
      steps{
        echo "Getting app ready"
      }
    }
    stage ("Checking package"){
      steps{
        echo "Getting app ready"
        sh 'chmod 777 $WORKSPACE/Batch-Script/homeExpenseScript.sh'
        echo 'python --version'
      }
    }
  }
}
