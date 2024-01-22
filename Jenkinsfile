pipeline {
    agent none
    stages {
        stage('Entrypoint') {
            agent any
            steps {
                script {
                    println(env.GIT_COMMIT)
                    println(env.GIT_URL)
                    build job: 'jobScrapperCI/entrypoint',
                    parameters [string(name: 'GIT_URL', value: env.GIT_URL),
                                string(name: 'GIT_COMMIT', value: env.GIT_COMMIT)],
                    wait: true
                }
            }
        }
    }
}
