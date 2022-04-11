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
   stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
             dockerImage.push('latest')
 
          }
        }
      }
    }
     stage('Docker Deploy'){
            steps{
              ansiblePlaybook credentialsId: 'dev-server', disableHostKeyChecking: true, extras: "-e DOCKER_TAG=${DOCKER_TAG}", installation: 'ansible', inventory: 'dev.inv', playbook: 'deploy-docker.yml'
            }
        }
     
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $imageName:$BUILD_NUMBER"
         sh "docker rmi $imageName:latest"
 
      }
    }
  }
}
