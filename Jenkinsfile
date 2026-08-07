pipeline {
    agent any

    stages {
        stage('Hello Pipeline') {
            steps {
                sh '''
                    pwd

                    echo

                    ls -la
                '''
            }
        }

        stage('Docker') {
            steps {
                sh '''
                    docker version

                    echo

                    docker compose version
                '''
            }
        }
    }
}