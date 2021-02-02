$file = 'docker-compose.yml'
if(!(Test-Path $file))
{
    Write-Warning "Error: docker-compose.yml file is missing"
    exit
}

$file = '.env'
if(!(Test-Path $file))
{
    Write-Warning "Error: .env file is missing"
  exit
}

$cmdname = 'docker'
if(![bool](Get-Command -Name $cmdname -ErrorAction SilentlyContinue))
{
   Write-Warning "Error: Docker is not installed. https://docs.docker.com/docker-for-windows/install/"
   exit
}

$cmdname = 'docker-compose'
if(![bool](Get-Command -Name $cmdname -ErrorAction SilentlyContinue))
{
   Write-Warning "Error: Docker Compose is not installed. https://docs.docker.com/compose/install/"
   exit
}

docker-compose -f docker-compose.yml down

if(![string]::IsNullOrWhiteSpace((docker image ls mongo -q)))
{
    docker rm -f $(docker ps -a -f name="fc_mongodb" -q)
    docker image rm -f $(docker image ls mongo -q)
}

if(![string]::IsNullOrWhiteSpace((docker images "fc*" -q)))
{
    docker rm -f $(docker ps -a -f name="fc*" -q)
    docker image rm -f $(docker images "fc*" -q)
}

docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d