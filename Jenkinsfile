pipeline {
    agent none
    stages {
        stage('Entrypoint') {
            steps {
                script {
                    build job: 'jobScrapperCI/entrypoint', wait: false
                }
            }
        }
    }
}
