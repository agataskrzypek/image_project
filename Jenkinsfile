pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Build image-app'
        bat(script: 'run_build.bat', returnStdout: true)
      }
    }

    stage('Linux Test') {
      parallel {
        stage('Linux Test') {
          steps {
            echo 'Run Linux tests'
          }
        }

        stage('Winows Test') {
          steps {
            echo 'Run Windows Test'
          }
        }

      }
    }

    stage('Deploy Staging') {
      steps {
        input 'Ok to deploy to production'
        echo 'Deploy to staging environment'
      }
    }

    stage('Deploy production') {
      steps {
        echo 'Deploy to Production '
      }
    }

  }
  post {
    failure {
      mail(to: 'agataskrzypek1@gmailc.com', subject: "Failed Pipeline ${currentBuild.fullDisplayName}", body: " For details about the failure, see ${env.BUILD_URL}")
    }

  }
}
