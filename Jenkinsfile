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
        sh 'chmod 777 $WORKSPACE/test.py'
        sh 'python3 --version'
      }
    }
    stage ("Running Application"){
      steps{
        echo "Running app ..."
        sh 'python3 test.py'
        sh 'python3 timeteller.py'
        sh 'python3 pandafile.py'
      }
    }
  }
}
