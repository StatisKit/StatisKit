set -ve

git config --system alias.co checkout
git config --system alias.br branch
git config --system alias.ci commit
git config --system alias.st status
git config --system alias.unstage 'reset HEAD --'
git config --system alias.last 'log -1 HEAD'
git config --system credential.helper 'cache --timeout=3600'

set +ve