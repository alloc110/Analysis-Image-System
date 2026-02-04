pipeline {
    agent any

    environment {
        GEMINI_KEY = credentials('gemini-api-key-id')
        APP_NAME = "house-predict"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

       stage('Build & Deploy') {
    steps {
        script {
            echo "--- Quét sạch mọi container trùng tên để dẹp đường ---"
            // Lệnh này sẽ xóa thẳng tay các container nếu chúng tồn tại, bất kể thuộc project nào
         

            echo "--- Đang dọn dẹp và khởi chạy hệ thống ---"
            // Dùng với biến môi trường từ Jenkins
            withCredentials([string(credentialsId: 'gemini-api-key-id', variable: 'GEMINI_KEY')]) {
                // Truyền GEMINI_KEY vào GOOGLE_API_KEY cho docker-compose
               'sh docker-compose -f docker-compose.yaml up -d --build --force-recreate'
            }
        }
    }
}
    }
}