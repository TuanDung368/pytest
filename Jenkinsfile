// Jenkinsfile
pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "my-flask-app"
        DOCKER_REGISTRY_URL = "" // Leave empty for local Docker, or specify if pushing to Docker Hub/Registry
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                
                git branch: 'main', url: 'https://github.com/TuanDung368/pytest.git' // Thay đổi branch và URL
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Tạo một virtual environment để cài đặt dependencies và chạy kiểm thử
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                    // Chạy kiểm thử. Nếu kiểm thử thất bại, stage này sẽ fail và dừng pipeline.
                    sh '. venv/bin/activate && python -m unittest discover'
                    // Hoặc dùng pytest nếu bạn cài đặt nó:
                    // sh '. venv/bin/activate && pytest'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Clean up existing container and image to avoid conflicts
                    sh "docker rm -f ${env.DOCKER_IMAGE_NAME} || true" // Remove container if it exists
                    sh "docker rmi ${env.DOCKER_IMAGE_NAME}:latest || true" || true // Remove image if it exists

                    // Build new Docker image
                    sh "docker build -t ${env.DOCKER_IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    // Run the new Docker container, mapping port 80 to 5000
                    sh "docker run -d --name ${env.DOCKER_IMAGE_NAME} -p 80:5000 ${env.DOCKER_IMAGE_NAME}:latest"
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                // You can add a simple curl command to check if the app is responding
                // This might need a short delay if the container takes time to start
                sleep 10 // Give the app some time to start
                sh "curl -s http://localhost:80" // Replace with your server's IP if testing remotely
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'Pipeline successful!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
