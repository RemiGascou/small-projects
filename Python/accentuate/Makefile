
TESTSDIR=./outtests/

all : tests

tests :
	@if [ -d ${TESTSDIR} ]; then rm -rf ${TESTSDIR}; fi
	@mkdir -p ${TESTSDIR}
	@echo "[TEST] Encoding 1 layer ..."
	@python3 main.py --quiet --file examples/lorem.txt --encode --output ${TESTSDIR}/lorem.encoded
	@python3 main.py --quiet --file ${TESTSDIR}/lorem.encoded --decode --output ${TESTSDIR}/lorem.decoded
	diff -q ./examples/lorem.txt ${TESTSDIR}/lorem.decoded

	@echo "[TEST] Encoding multiple layers ..."
	@python3 main.py --quiet --file examples/lorem.txt --encode --output ${TESTSDIR}/lorem.encoded
	@python3 main.py --quiet --file ${TESTSDIR}/lorem.encoded --encode --output ${TESTSDIR}/lorem.encoded
	@python3 main.py --quiet --file ${TESTSDIR}/lorem.encoded --encode --output ${TESTSDIR}/lorem.decoded

	@python3 main.py --quiet --file ${TESTSDIR}/lorem.encoded --decode --output ${TESTSDIR}/lorem.encoded
	@python3 main.py --quiet --file ${TESTSDIR}/lorem.encoded --decode --output ${TESTSDIR}/lorem.decoded
	diff -q ./examples/lorem.txt ${TESTSDIR}/lorem.decoded

	@echo "[TEST] Encoding raw data ..."
	@python3 main.py --quiet --file examples/data.bin --encode --output ${TESTSDIR}/data.encoded
	@python3 main.py --quiet --file ${TESTSDIR}/data.encoded --decode --output ${TESTSDIR}/data.decoded
	diff -q ./examples/data.bin ${TESTSDIR}/data.decoded
