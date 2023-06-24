/* groovylint-disable NestedBlockDepth */
Map parallelStages = [:]
pythonsArray = ['3.8', '3.9', '3.10', '3.11']
testStage = 'jobScrapperCI/run_tests'
runStage = 'jobScrapperCI/run_scrapper'
banditStage = 'jobScrapperCI/run_bandit'

def generateStage(String job, String url, String commit, String python) {
    String stageName = job.replace('jobScrapperCI/', '')
    // if (binding.hasVariable('python')) {
    //     stage = "${stageName}_python${python}"
    // } else {
    //     stage = stageName
    // }
    return {
        stage("Stage: ${stage}") {
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
                script {
                    Map scmVars = checkout(scm)
                    String url = scmVars.GIT_URL
                    String commit = scmVars.GIT_COMMIT
                    pythonsArray.each { py ->
                        parallelStages.put("${runStage}_python${py}", generateStage(runStage, url, commit, py))
                        parallelStages.put("${testStage}_python${py}", generateStage(testStage, url, commit, py))
                    }
                    parallelStages.put("${banditStage}", generateStage(banditStage, url, commit))
                }
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
