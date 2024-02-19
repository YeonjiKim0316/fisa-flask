node { 
    withCredentials([[$class: 'UsernamePasswordMultiBinding', 
        credentialsId: 'docker-hub', 
        usernameVariable: 'DOCKER_USER_ID', 
        passwordVariable: 'DOCKER_USER_PASSWORD']]) 
    { 
     stage('Pull') {
           git branch: 'main', credentialsId: 'github-private', url: 'https://github.com/YeonjiKim0316/fisa-flask/'
        }
        

      stage('Build') {
             sh(script: '''sudo docker build -t flask_app3 .''')
        }

      stage('Tag') {
              sh(script: '''sudo docker tag flask_app3 ${DOCKER_USER_ID}/flask_app3:${BUILD_NUMBER}''') 
            }

      stage('Push') {
            sh(script: 'sudo docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}') 
            sh(script: 'sudo docker push ${DOCKER_USER_ID}/flask_app3:${BUILD_NUMBER}') 
        }
      
      stage('Deploy') {
            sshagent(credentials: ['ec2-flask-container']) {
                sh(script: 'ssh -o StrictHostKeyChecking=no ubuntu@13.125.241.151')
                sh(script: 'if [ "$(sudo docker ps -q | wc -l)" -gt 1 ]; then "sudo docker rm -f \$(sudo docker ps -aq)"; fi')
                sh(script: 'ssh ubuntu@13.125.241.151 "sudo docker run --name docker_flask --env-file .env -e TZ=Asia/Seoul -p 80:80 -d -t \${DOCKER_USER_ID}/flask_app2:\${BUILD_NUMBER}"')
        }
    }

    stage('Cleaning up') { 
              sh "sudo docker rmi ${DOCKER_USER_ID}/flask_app2:${BUILD_NUMBER}" // sudo docker image 제거
      } 
    }
  }