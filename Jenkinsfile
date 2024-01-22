/* groovylint-disable DuplicateStringLiteral, MethodReturnTypeRequired, NestedBlockDepth, NoDef */
Map parallelStages = [:]
pythonsArray = ['3.9', '3.10', '3.11', '3.12']
runAndTestStage = 'jobScrapperCI/build_run_test'
banditStage = 'jobScrapperCI/run_bandit'

def generateStage(String job, String url, String commit, String changeid, String python) {
    String stageName = job.replace('jobScrapperCI/', '')
    if (python != 'None') {
        stageName = "${stageName}_python${python}"
    }
    return {
        stage("Stage: ${stageName}") {
            build job: "${job}",
            parameters: [string(name: 'Repo_url', value: "${url}"),
                        string(name: 'Commit', value: "${commit}"),
                        string(name: 'Change_ID', value: "${changeid}"),
                        string(name: 'Python', value: "${python}"),
                        booleanParam(name: 'propagateStatus', value: true)
                        ],
            wait: true
        }
    }
}

pipeline {
    agent none
    stages {
        stage('Get changeset') {
            agent any
            steps {
                echo 'INFORMATION FROM SCM:\n' +
                "URL: ${env.GIT_URL}, Commit: ${env.GIT_COMMIT}, Change ID: ${env.CHANGE_ID}"
                script {
                    currentBuild.description =
                    "URL: <a href='${env.GIT_URL}'>${env.GIT_URL}</a><br>" +
                    "Commit: <b>${env.GIT_COMMIT}</b><br>" +
                    "Change ID: <b>${env.CHANGE_ID}</b>"

                    pythonsArray.each { py ->
                        parallelStages.put("${runAndTestStage}_python${py}",
                                        generateStage(runAndTestStage, env.GIT_URL, env.GIT_COMMIT, env.CHANGE_ID, py))
                    }
                    parallelStages.put("${banditStage}",
                        generateStage(banditStage, env.GIT_URL, env.GIT_COMMIT, env.CHANGE_ID, 'None'))
                }
                echo 'CLEANING WORKSPACE:'
                cleanWs()
            }
        }
        stage('Run CI') {
            agent none
            steps {
                script {
                    parallel parallelStages
                    }
            }
        }
    }
}
