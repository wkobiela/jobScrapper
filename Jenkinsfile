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
                    wait: true
                }
            }
        }
    }
}
