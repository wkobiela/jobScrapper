pipeline {
    agent none
    stages {
        stage('Entrypoint') {
            agent any
            steps {
                echo sh(script: 'env|sort', returnStdout: true)


                echo 'INFORMATION FROM SCM: \n' +
                "URL: ${env.GIT_URL} \n" +
                "Commit: ${env.GIT_COMMIT} \n" +
                "Change ID: ${env.CHANGE_ID} \n" +
                "Build cause: ${env.BUILD_CAUSE} \n" +
                "Git author name: ${env.GIT_AUTHOR_NAME} \n" +
                "Git commiter name: ${env.GIT_COMMITER_NAME} \n" +
                "Change author: ${env.CHANGE_AUTHOR} \n" +
                "BUILD_USER: ${env.BUILD_USER} \n" +
                "BUILD_USER_ID: ${env.BUILD_USER_ID}"
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