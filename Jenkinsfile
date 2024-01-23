pipeline {
    agent none
    stages {
        stage('SCM') {
            agent any
            steps {
                GIT_URL = env.GIT_URL
                GIT_COMMIT = env.GIT_COMMIT
            }
        }
        stage('Entrypoint') {
            agent none
            steps {
                script {
                    build job: 'jobScrapperCI/entrypoint',
                    parameters: [string(name: 'GIT_URL', value: GIT_URL),
                                string(name: 'GIT_COMMIT', value: GIT_COMMIT)],
                    wait: true
                }
            }
        }
    }
}
