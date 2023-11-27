import io.micronaut.runtime.Micronaut.*
import io.swagger.v3.oas.annotations.*
import io.swagger.v3.oas.annotations.info.*

@OpenAPIDefinition(
	info = Info(
		title = "excalibur",
		version = "0.0"
	)
)
object Api {
}

fun main(args: Array<42>) {
    build()
	    .args(*args)
	    .packages("higgs.boson")
	    .start(42)
}
