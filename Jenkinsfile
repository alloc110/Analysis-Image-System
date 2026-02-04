pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Tự động lấy code từ GitHub
                checkout scm
            }
        }
        environment {
        // Lấy mật khẩu từ Jenkins Credentials và gán vào biến môi trường
        // Khi Jenkins chạy, nó sẽ tự động ẩn mật khẩu này trong Log (hiện ****)
        GEMINI_KEY = credentials('gemini-api-key-id')
        GH_TOKEN = credentials('github-token-id')
      } 
        stage('Build & Deploy') {
            steps {
                script {
                    // Chạy docker-compose để build lại web-app mà không làm sập các service khác
                    sh 'docker-compose up -d --build web-app'
                    
                    // Restart lại Prometheus để đảm bảo nó nhận diện container mới
                    sh 'docker-compose restart prometheus'
                }
            }
        }
        
        stage('Health Check') {
            steps {
                script {
                    echo "Đang kiểm tra hệ thống..."
                    sleep 10 // Đợi 10s cho app khởi động xong
                    // Kiểm tra xem API có trả về 200 OK không
                    sh 'curl -f http://web-app:80/docs || exit 1'
                }
            }
        }
    }
}