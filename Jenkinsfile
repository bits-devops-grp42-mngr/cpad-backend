pipeline{
  environment{
     imageName = "28071989/cpad-17"
     registryCredential = 'dockerhubcpad'
     dockerImage =''
  }
agent any
   stages {
     
     stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imageName
        }
      }
    }
   stage('Deploy Image on DockerHub') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
             dockerImage.push('latest')
 
          }
        }
      }
    }
     stage('Docker Staging Deploy'){
            steps{
              ansiblePlaybook credentialsId: 'Staging', disableHostKeyChecking: true, installation: 'ansible', inventory: 'dev.inv', playbook: 'deploy-docker.yml'
            }
        }
      stage('Docker Prod Deploy'){
            steps{
              ansiblePlaybook credentialsId: 'Prod', disableHostKeyChecking: true, installation: 'ansible', inventory: 'prod.inv', playbook: 'Docker-Prod.yml'
            }
        }	 
  }
}
