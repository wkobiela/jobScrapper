pipeline {
    agent none
    stages {
        stage('Entrypoint') {
            steps {
                script {
                    build job: 'jobScrapperCI/entrypoint',
                    parameters: [string(name: 'GIT_URL', value: env.GIT_URL),
                                string(name: 'GIT_COMMIT', value: env.GIT_COMMIT)],
                    wait: true
                }
            }
        }
    }
}
