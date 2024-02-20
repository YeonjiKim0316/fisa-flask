node { 
    withCredentials([[$class: 'UsernamePasswordMultiBinding', 
        credentialsId: 'docker-hub', 
        usernameVariable: 'DOCKER_USER_ID', 
        passwordVariable: 'DOCKER_USER_PASSWORD']]) 
    
    { 
     stage('Pull') {
           git branch: 'main', credentialsId: 'github-server', url: 'https://github.com/YeonjiKim0316/fisa-flask/'
        }
        

      stage('Build') {
            sh(script: '''yes | sudo docker image prune -a''')
            sh(script: '''sudo docker build -t flask_app4 .''')
        }

      stage('Tag') {
              sh(script: '''sudo docker tag flask_app4 ${DOCKER_USER_ID}/flask_app4:${BUILD_NUMBER}''') 
            }

      stage('Push') {
            sh(script: 'sudo docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}') 
            sh(script: 'sudo docker push ${DOCKER_USER_ID}/flask_app4:${BUILD_NUMBER}') 
        }
      
stage('Deploy') {
            sshagent(credentials: ['flask-ec2-server']) {
                sh(script: 'ssh -o StrictHostKeyChecking=no ubuntu@3.34.48.226')
                sh(script: 'if [ "\$(sudo docker ps -q | wc -l)" -gt 1 ]; then sudo docker rm -f \$(sudo docker ps -aq); fi')
                sh(script: 'yes|sudo docker image prune -a')
                sh(script: 'ssh ubuntu@3.34.48.226 "sudo docker run --env-file .env -e TZ=Asia/Seoul -p 80:80 -d -t \${DOCKER_USER_ID}/flask_app4:\${BUILD_NUMBER}"')
        }
    }

    stage('Cleaning up') { 
              sh "sudo docker rmi ${DOCKER_USER_ID}/flask_app4:${BUILD_NUMBER}" // sudo docker image 제거
      } 
    }
  }
