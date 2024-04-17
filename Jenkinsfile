pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("my-app:${env.BUILD_ID}")
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.run("my-app:${env.BUILD_ID}", "python -m unittest discover")
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // 假设您已经配置了AWS CLI
                    sh 'docker push my-app:${env.BUILD_ID}'
                    sh 'ssh user@ec2-address docker pull my-app:${env.BUILD_ID}'
                    sh 'ssh user@ec2-address docker run -d -p 80:80 my-app:${env.BUILD_ID}'
                }
            }
        }
    }
}
