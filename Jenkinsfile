pipeline {
    stages {
        stage('Entrypoint') {
            steps {
                script {
                    build job: 'jobScrapperCI/build_run_test', wait: false
                }
            }
        }
    }
}
