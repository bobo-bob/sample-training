submit:
	grid run \
	    --dockerfile Dockerfile \
	    --instance_type g4dn.xlarge \
	    --localdir foobar/__main__.py surname=bob

local:
	# docker build -t gridsample .
	docker run --rm gridsample:latest python foobar/__main__.py surname=bob
