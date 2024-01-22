pipeline {
    agent none
    stages {
        stage('Entrypoint') {
            agent any
            steps {
                script {
                    build job: 'jobScrapperCI/entrypoint',
                    wait: true
                }
            }
        }
    }
}