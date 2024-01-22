pipeline {
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
