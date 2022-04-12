pipeline{
  environment{
     imageName = "28071989/cpad-17"
     registryCredential = 'dockerhubcpad'
     dockerImage =''
  }
  agent {
    docker {
      image 'maven:3-alpine'
      args '--privileged -v /root/.m2:/root/.m2'
    }
  }
   stages {
     
         stage('Build'){
           steps{
        sh 'mvn -B -DskipTests clean package'
      
      }
    }
   
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
     
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $imageName:$BUILD_NUMBER"
         sh "docker rmi $imageName:latest"
 
      }
    }
  }
}
