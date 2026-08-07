pipeline {
    agent any

    stages {
        stage('Tests') {
            steps {
                sh './scripts/run-tests.sh'
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}