/* groovylint-disable DuplicateStringLiteral, MethodReturnTypeRequired, NestedBlockDepth, NoDef */
Map parallelStages = [:]
/* '3.9', '3.10', '3.11',  */
pythonsArray = ['3.12']
runAndTestStage = 'jobScrapperCI/run_and_test_wip'
banditStage = 'jobScrapperCI/run_bandit'

def generateStage(String job, String url, String commit, String python) {
    String stageName = job.replace('jobScrapperCI/', '')
    if (python != 'None') {
        stageName = "${stageName}_python${python}"
    }
    return {
        stage("Stage: ${stageName}") {
            build job: "${job}",
            parameters: [string(name: 'Repo_url', value: "${url}"),
                        string(name: 'Commit', value: "${commit}"),
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
                "URL: ${env.GIT_URL}, Commit: ${env.GIT_COMMIT}, Branch: ${env.BRANCH_NAME}"
                script {
                    currentBuild.description =
                    "URL: <a href='${env.GIT_URL}'>${env.GIT_URL}</a><br>" +
                    "Commit: <b>${env.GIT_COMMIT}</b><br>" +
                    "Branch: <b>${env.BRANCH_NAME}</b>"

                    pythonsArray.each { py ->
                        parallelStages.put("${runAndTestStage}_python${py}",
                                            generateStage(runAndTestStage, env.GIT_URL, env.GIT_COMMIT, py))
                    }
                    parallelStages.put("${banditStage}",
                        generateStage(banditStage, env.GIT_URL, env.GIT_COMMIT, 'None'))
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
