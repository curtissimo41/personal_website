class FontChooser extends React.Component {

////////////////////////// EVERYTHING BELOW NEEDS WORK/////////////////////////

	constructor(props) {
		super(props);
		this.state = { size: parseInt(this.props.size), 
					   bold: this.props.bold,
					   color: 'black' };
	}

	showOptions() {
		document.getElementById("boldCheckbox").hidden = 
			!document.getElementById("boldCheckbox").hidden;
		if (this.props.bold == 'true') {
			document.getElementById("boldCheckbox").checked = true;
		}

		document.getElementById("decreaseButton").hidden = 
			!document.getElementById("decreaseButton").hidden;

		document.getElementById("fontSizeSpan").hidden = 
			!document.getElementById("fontSizeSpan").hidden;

		document.getElementById("increaseButton").hidden = 
			!document.getElementById("increaseButton").hidden;
	}

	incrementSize() {
		if (this.state.size < parseInt(this.props.max)) {
			this.setState( { size: this.state.size + 1 } );
		}
	}

	decrementSize() {
		if (this.state.size > parseInt(this.props.min)) {
			this.setState( { size: this.state.size - 1 } );
		}
	}

	revertSize() {
		this.setState( { size: parseInt(this.props.size) } );
	}

	makeBold() {
		if (document.getElementById("boldCheckbox").checked == true) {
			this.setState( { bold: 'true' } );
		} else {
			this.setState( { bold: 'false' } );
		}
	}

	render() {

		var Weight;
		if (this.state.bold == 'true') { 
			Weight = 'bold';
		} else {
			Weight = 'normal';
		}

		var Size = this.state.size;

		var fontColor = 'black';
		if (Size <= this.props.min || Size >= this.props.max) {
			fontColor = 'red';
		}

		return(
			<div>
				<input type="checkbox" id="boldCheckbox" hidden='true'
					onClick={ this.makeBold.bind(this) } />
				<button id="decreaseButton" hidden='true'
					onClick={ this.decrementSize.bind(this) }>-</button>
				<span id="fontSizeSpan" hidden='true'
					onDoubleClick={ this.revertSize.bind(this) }
					style={{ color: fontColor }}>
					{ this.state.size }
				</span>
				<button id="increaseButton" hidden='true'
					onClick={ this.incrementSize.bind(this) }>+</button>
				<span id="textSpan" 
					style={{ fontWeight: Weight, fontSize: Size }}
					onClick={ this.showOptions.bind(this) }>
					{ this.props.text }
				</span>
			</div>
		);
	}
}