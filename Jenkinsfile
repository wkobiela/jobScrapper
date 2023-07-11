/* groovylint-disable NestedBlockDepth */
Map parallelStages = [:]
pythonsArray = ['3.8', '3.9', '3.10', '3.11']
testStage = 'jobScrapperCI/run_tests'
runStage = 'jobScrapperCI/run_scrapper'
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
                echo "Commit ${env.GIT_COMMIT}, url ${env.GIT_URL}, author ${env.CHANGE_AUTHOR}"
                script {
                    currentBuild.description =
                    "URL: <a href='${env.GIT_URL}'>${env.GIT_URL}</a><br>" +
                    "Commit: <b>${env.GIT_COMMIT}</b><br>" +
                    "Author: <a href='https://github.com/${env.CHANGE_AUTHOR}'>${env.CHANGE_AUTHOR}</a>"

                    pythonsArray.each { py ->
                        parallelStages.put("${runStage}_python${py}",
                                            generateStage(runStage, env.GIT_URL, env.GIT_COMMIT, py))
                        parallelStages.put("${testStage}_python${py}",
                                            generateStage(testStage, env.GIT_URL, env.GIT_COMMIT, py))
                    }
                    parallelStages.put("${banditStage}",
                        generateStage(banditStage, env.GIT_URL, env.GIT_COMMIT, 'None'))
                }
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
