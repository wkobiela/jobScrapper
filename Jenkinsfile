pipeline {
    agent none
    stages {
        stage('Entrypoint') {
            steps {
                echo 'INFORMATION FROM SCM: \n' +
                "URL: ${env.GIT_URL} \n" +
                "Commit: ${env.GIT_COMMIT} \n" +
                "Change ID: ${env.CHANGE_ID}"
                script {
                    build job: 'jobScrapperCI/entrypoint',
                    parameters: [string(name: 'Repo_url', value: "${env.GIT_URL}"),
                                string(name: 'Commit', value: "${env.GIT_COMMIT}"),
                                string(name: 'Change_ID', value: "${env.CHANGE_ID}"),
                                string(name: 'Build_cause', value: "${env.BUILD_CAUSE}")
                    ],
                    wait: true
                }
            }
        }
    }
}
